var tress = require('tress');
var needle = require('needle'); //instead of got library
var cheerio = require('cheerio');
var fs = require('fs');

var URL = 'https://poizdato.net/rozklad-po-stantsii/kyiv-pas/';
var results = [];
var obj = {};

var q = tress(function (url, callback) {
    needle.get(url, function (err, res) {
        if (err) throw err;
        var $ = cheerio.load(res.body);
        if (url == 'https://poizdato.net/rozklad-po-stantsii/kyiv-pas/')
            $('*').map((elem) => {
                if ($('*')[elem]['name'] == 'a')
                    if ((/hrafik-rukhu(.*?)$/).test($('*')[elem]['attribs']['href']))
                        q.push('https://poizdato.net' + $('*')[elem]['attribs']['href'])
            })
        else {
            obj[url] = []
            $("option").map((e) => {
                obj[url].push($("option")[e]["children"][0]['data'])
            })
            results.push(obj)
        }
        callback();
    });
}, 200);

q.drain = function () {
    fs.writeFileSync('./data.json', JSON.stringify(results));
}

q.push(URL);