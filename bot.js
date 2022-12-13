require("dotenv").config()

const { Telegraf } = require("telegraf");
const got = require("got");
const cheerio = require("cheerio");

const { getHtml, parse } = require("./parseSite");

const bot = new Telegraf(process.env.BOT_TOKEN)

async function launchBot(lastTitle) {
    const $ = await getHtml()

    const info = await parse($)

    const text = `<b>${info.title}</b>\n\n${info.description.trim()}`

    if (info.title != lastTitle) {
        const link = $(".l-list__item").eq(0).find("a.c-card-list__link").attr('href')

        res = await got.get(link);
        res = cheerio.load(res.body)
        img = res(".c-post__preview-picture").find("img").attr("src")

        bot.telegram.sendPhoto(-1001821022552, img, {
            caption: text,
            parse_mode: "HTML"
        })
    }

    console.log(1)

    setTimeout(launchBot, 60000, info.title)
}

launchBot("")