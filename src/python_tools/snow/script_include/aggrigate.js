try {
    var agg = new GlideAggregate('cmdb_software_product_model');
    var queryString = 'application_model=35989b9183a69210bef196a6feaad3b6';
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
} catch (ex) {
    var message = ex + '';
    gs.debug('caught exception=' + message);
}
// https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0852541