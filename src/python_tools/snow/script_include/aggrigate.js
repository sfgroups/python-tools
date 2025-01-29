function getSysIdByAppName(appName) {
    if (!appName || typeof appName !== 'string') {
        return 'Invalid application name';
    }
    var trimmedAppName = appName.trim(); // Trim leading and trailing spaces

    var gr = new GlideRecord('cmdb_application_product_model');
    gr.addQuery('name', appName);
    gr.query();

    if (gr.next()) {
        return gr.getValue('sys_id');
    } else {
        return 'No matching record found';
    }
}


try {
    var appName = 'Clear Path';
    var sysId = getSysIdByAppName(appName);
    gs.info('Sys ID: ' + sysId);
    var sysIdRegex = /^[0-9a-f]{32}$/;
    if (!sysIdRegex.test(sysId)) {
        gs.error("invalid sysId");
    } else {
        var agg = new GlideAggregate('cmdb_software_product_model');
        var queryString = 'application_model=' + sysId;
        var isValidQuery = agg.isValidEncodedQuery(queryString);
        if (isValidQuery) {
            agg.addEncodedQuery(queryString);
            agg.addAggregate('MAX', 'version');
            agg.setGroup(false);
            agg.query();

            while (agg.next()) {
                var maxValue = agg.getAggregate('MAX', 'version');
                gs.info('Maximum version: ' + maxValue);
            }
        } else {
            throw "Encoded query is invalid. Please check and update the script";
        }
    }
} catch (ex) {
    var message = ex + '';
    gs.debug('caught exception=' + message);
}
// https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0852541