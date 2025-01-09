var gr = new GlideRecord('incident');
gr.addQuery('priority', 1);
gr.query();
while (gr.next()) {
    gs.print("Incident Number: " + gr.number);
}
