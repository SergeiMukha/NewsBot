const cheerio = require("cheerio");
const axios = require("axios");

async function getHtml(url) {
    const res = await axios.get(url, {
        headers: {
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }
    })

    console.log(1)
}

async function parse() {
    const res = await getHtml("https://www.ukr.net/ua/");
}

parse()

console.log(1)