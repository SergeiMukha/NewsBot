require("dotenv").config({
    path: "../../.env"
})

const { Telegraf } = require("telegraf");
const got = require("got");
const cheerio = require("cheerio");

const { getHtml, parse } = require("./parseSite");

// Create Bot
const bot = new Telegraf(process.env.BOT_TOKEN_JS)

// Launch Bot
async function launchBot(lastTitle) {
    // Get Page Html
    const $ = await getHtml()

    // Parse Html
    const info = await parse($)

    // Form Message Text
    const text = `<b>${info.title}</b>\n\n${info.description.trim()}`

    // Checking if this news is new
    if (info.title != lastTitle) {
        // Getting News Page To Grab And Parse The Photo in Normal Resolution
        const link = $(".l-list__item").eq(0).find("a.c-card-list__link").attr('href')

        res = await got.get(link);
        res = cheerio.load(res.body)
        img = res(".c-post__preview-picture").find("img").attr("src")

        // Sending Message
        bot.telegram.sendPhoto(-1001821022552, img, {
            caption: text,
            parse_mode: "HTML"
        })
    }

    setTimeout(launchBot, 60000, info.title)
}

launchBot("")