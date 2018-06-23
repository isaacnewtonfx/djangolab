<div class="col-sm-6">

    <?php if(logged_in()){ ?>
	    <h2 style="color: rgba(149, 149, 149, 0.80);">Change Password</h2><br/>
    <?php }else{ ?>
        <h2>Change Password</h2><br/>
    <?php } ?>

	<!--Show notification messages here -->
	<div style="margin:5px auto;" class="alert alert-warning alert-dismissible" role="alert"

        <?php
            $has_flash_msg = $this->session->flashdata('msg');
            $has_status_msg = isset($msg);
            if( $has_flash_msg || $has_status_msg ){echo "";}else{ echo "hidden"; }
		?>
    >
    <button type="button" class="close" data-dismiss="alert">
        <span aria-hidden="true">&times;</span>
        <span class="sr-only">Close</span>
    </button>

    <p>
        <?php
            if ($has_flash_msg){
                echo "<p> <b>$has_flash_msg</b></p>";
            }elseif($has_status_msg){
                echo "<p><b>$msg</b></p>";
            }
        ?>
    </p>

    </div>

    <?php echo form_open(); ?>
    New Password:<br />
    <input type="password" name="new_password" value="<?php echo set_value('new_password'); ?>" size="50" class="form-control" />
    <?php echo form_error('new_password','<div class="alert-danger">', '</div>'); ?><br />

    Repeat New Password:<br />
    <input type="password" name="new_password_repeat" value="<?php echo set_value('new_password_repeat'); ?>" size="50" class="form-control" />
    <?php echo form_error('password','<div class="alert-danger">', '</div>'); ?><br />

    <br />
    <input class="btn btn-primary" type="submit" value="Submit" name="Submit" />

</form>

</div>
