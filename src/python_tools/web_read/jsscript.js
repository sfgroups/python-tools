const {readFileSync, writeFile, existsSync, promises: fsPromises, symlinkSync} = require('fs');
const { exit } = require('process');

const myArgs = process.argv.slice(2);
if (myArgs.length === 0) { 
    console.log("filename required!") 
    exit(1);
}
filename=myArgs[0]
if (existsSync(filename)) {
    console.log("exists:", filename);
  } else {
    console.log("DOES NOT exist:", filename);
    exit(1);
  }

outputfile=filename.replace('.html','.pdf')

var data=readFileSync(filename, 'utf-8')
var DOMParser = require('xmldom').DOMParser;
var parser = new DOMParser();
const virtualDoc = parser.parseFromString(data, 'text/html');

var elem = virtualDoc.getElementsByTagName('embed')[0];
for (var i = 0; i < elem.attributes.length; i++) {
    var attrib = elem.attributes[i];
    if (attrib.specified) {
        if( attrib.name == "src") {
            var result =attrib.value
            result=result.replace('data:application/pdf;base64,','');           
            let buff = Buffer.from(decodeURIComponent(result), 'base64');
            writeFile(outputfile, buff, err => {
                if (err) {
                  console.error(err);
                }               
              });            
        }
    }
}