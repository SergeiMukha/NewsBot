const got = require('got');
const cheerio = require("cheerio");

// Get Page Html
async function getHtml() {
  const data = await got.get('https://focus.ua/news')

  return cheerio.load(data.body);
}

// Parse Html
async function parse($) {

    const title = $(".l-list__item").eq(0).find(".c-card-list__link").text();
    const description = $(".l-list__item").eq(0).find(".c-card-list__description").text();

    return {title: title, description: description}
}

module.exports = {
    getHtml,
    parse
}