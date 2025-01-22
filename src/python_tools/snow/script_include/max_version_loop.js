try {
    var gr = new GlideRecord('cmdb_software_product_model');
    var queryString = 'application_model=35989b9183a69210bef196a6feaad3b6';

    var isValidQuery = gr.isValidEncodedQuery(queryString);
    if (isValidQuery) {
        gr.addEncodedQuery(queryString);
        gr.orderByDesc('version'); // Orders records in descending order
        gr.query();

        if (gr.next()) { // Retrieve the first record, which has the max version
            gs.info('Max Version: ' + gr.version);
        } else {
            gs.info('No records found matching the query.');
        }
    } else {
        throw "Encoded query is invalid. Please check and update the script.";
    }
} catch (ex) {
    var message = ex + '';
    gs.error('Caught exception: ' + message);
}
