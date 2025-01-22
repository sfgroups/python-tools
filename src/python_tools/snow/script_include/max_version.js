try {
    var gr = new GlideRecord('cmdb_software_product_model');
    var queryString = 'application_model=35989b9183a69210bef196a6feaad3b6';

    // Validate the encoded query
    var isValidQuery = gr.isValidEncodedQuery(queryString);
    if (isValidQuery) {
        gr.addEncodedQuery(queryString);
        gr.query();

        var maxVersion = null;

        // Iterate through records to find the highest semantic version
        while (gr.next()) {
            if (!maxVersion || compareVersions(gr.version.toString(), maxVersion) > 0) {
                maxVersion = gr.version.toString();
            }
        }

        if (maxVersion) {
            gs.info('Max Version: ' + maxVersion);
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

/**
 * Compare two semantic version strings (e.g., "1.0.0" and "2.1.3").
 * Returns:
 *   -1 if versionA < versionB
 *    0 if versionA == versionB
 *    1 if versionA > versionB
 */
function compareVersions(versionA, versionB) {
    var aParts = versionA.split('.').map(Number);
    var bParts = versionB.split('.').map(Number);

    for (var i = 0; i < Math.max(aParts.length, bParts.length); i++) {
        var a = aParts[i] || 0;
        var b = bParts[i] || 0;

        if (a < b) return -1;
        if (a > b) return 1;
    }
    return 0;
}
