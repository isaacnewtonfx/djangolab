from django.core.serializers import serialize
from .models import places
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl.query import MultiMatch, Match
from elasticsearch_dsl import Search,Q
from elasticsearch_dsl import Document
from elasticsearch import Elasticsearch


connections.create_connection(
    hosts=['https://elastic:I6qQrHyNPW7jf2ffJsLLmfS4@26c229ea50544380ba0130fe3389d810.us-east-1.aws.found.io:9243'],
    verify_certs=False,
    use_ssl=True
)


# This function is for reading PostgreSQL Table, converting each row into GeoJSON and indexing it into ElasticSearch
def pg2es():

    Doc = Document()

    for row in places.objects.all():
        geojson = serialize('geojson', [row], geometry_field='geom')

        Doc.save(index = "places2")

        print(geojson)    


def search(terms):
    s = Search(index="places")
    q = MultiMatch(query=terms, fields=["properties.Place_Type",
                                        "properties.Floor", 
                                        "properties.Room^3", 
                                        "properties.Address"],
                                        analyzer = "standard",
                                        tie_breaker = 0.6)
    s = s.query(query)
    res = s.execute()
    print(res)