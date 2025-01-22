(function executeClientScript() {
    var sysId = g_form.getValue('u_manager');
    var displayValue = g_form.getDisplayValue('u_manager');

    console.log('Sys ID:', sysId);
    console.log('Display Value:', displayValue);

    alert('Selected Manager: ' + displayValue);
})();
