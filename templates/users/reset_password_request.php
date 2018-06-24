<div class="col-sm-6">
	<h2>Reset Password</h2>
	<br/>

	<!--Show notification messages here -->
	<?php echo show_status_msg(); ?>

		<?php echo form_open(); ?>

			Please, provide us your Email:<br />
			<input type="email" name="email" size="50" class="form-control" value="<?php echo set_value('email'); ?>" />
			<?php echo form_error('email','<div class="alert-danger">', '</div>'); ?><br />

			<input class="btn btn-primary" type="submit" value="Submit" name="Submit" />

		</form>

</div>
