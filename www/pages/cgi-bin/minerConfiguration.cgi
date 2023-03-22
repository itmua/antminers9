
cat <<EOT
<script>
function f_submit_miner_conf() {
	_ant_freq = "18:218.75:1106";
	_ant_voltage = "0725";
	try
	{
		_ant_freq = ant_data["bitmain-freq"];
		_ant_voltage = ant_data["bitmain-voltage"];
	}
	catch(err)
	{
		alert('Invalid Miner configuration file. Edit manually or reset to default.');
	}
	
	_ant_pool1url = jQuery("#ant_pool1url").val();
	_ant_pool1user = jQuery("#ant_pool1user").val();
	_ant_pool1pw = jQuery("#ant_pool1pw").val();
	_ant_pool2url = jQuery("#ant_pool2url").val();
	_ant_pool2user = jQuery("#ant_pool2user").val();
	_ant_pool2pw = jQuery("#ant_pool2pw").val();
	_ant_pool3url = jQuery("#ant_pool3url").val();
	_ant_pool3user = jQuery("#ant_pool3user").val();
	_ant_pool3pw = jQuery("#ant_pool3pw").val();
	_ant_nobeeper = "false";
	_ant_notempoverctrl = "false";
	_ant_fan_customize_switch = "false";
	_ant_fan_customize_value = jQuery("#ant_fan_customize_value").val();
	
	if(document.getElementById("ant_beeper").checked) {
		_ant_nobeeper = "false";
	} else {
		_ant_nobeeper = "true";
	}
	if(document.getElementById("ant_tempoverctrl").checked) {
		_ant_notempoverctrl = "false";
	} else {
		_ant_notempoverctrl = "true";
	}

	if(document.getElementById("ant_fan_customize_switch").checked) {
		_ant_fan_customize_switch= "true";
		
	} else {
		_ant_fan_customize_switch= "false";
	}

	_ant_freq=jQuery("#ant_freq").val();
	jQuery("#cbi_apply_bmminer_fieldset").show();
	
	jQuery.ajax({
		url: '/cgi-bin/set_miner_confstok.cgi',
		type: 'POST',
		dataType: 'json',
		timeout: 30000,
		cache: false,
		data: {_ant_pool1url:_ant_pool1url, _ant_pool1user:_ant_pool1user, _ant_pool1pw:_ant_pool1pw,_ant_pool2url:_ant_pool2url, _ant_pool2user:_ant_pool2user, _ant_pool2pw:_ant_pool2pw,_ant_pool3url:_ant_pool3url, _ant_pool3user:_ant_pool3user, _ant_pool3pw:_ant_pool3pw, _ant_nobeeper:_ant_nobeeper, _ant_notempoverctrl:_ant_notempoverctrl,_ant_fan_customize_switch:_ant_fan_customize_switch,_ant_fan_customize_value:_ant_fan_customize_value, _ant_freq:_ant_freq, _ant_voltage:_ant_voltage},
		success: function(data) {
			window.location.reload();
		},
		error: function() {
			window.location.reload();
		}
	});
}

jQuery(document).ready(function() {
	f_get_miner_conf();
});
</script>
EOT

