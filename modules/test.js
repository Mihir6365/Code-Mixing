const axios = require('axios');
const jsdom = require("jsdom");
const { JSDOM } = jsdom;
const express = require('express')
const app = express()
const port = 3000
const cors = require('cors');
app.use(cors());
const fetchTranslation = async (input) => {
    let encodedInput = encodeURIComponent(input);
    try {
        const response = await axios({
            url: "https://www.google.com/async/translate",
            method: 'POST',
            headers: {
                "accept": "*/*",
                "accept-language": "en-IN,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6",
                "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
                "sec-ch-ua": "\"Not A(Brand\";v=\"99\", \"Google Chrome\";v=\"121\", \"Chromium\";v=\"121\"",
                "cookie": "SEARCH_SAMESITE=...; NID=511=...", // Your long cookie string
                "Referer": "https://www.google.com/",
                "Referrer-Policy": "origin"
            },
            data: `async=translate,sl:auto,tl:en,st:${encodedInput},id:1708618826648,qc:true,ac:true,_id:tw-async-translate,_pms:s,_fmt:pc`,
        });

        const data = (response.data);
        const dom = new JSDOM(data);
        const sourceText = input;
        const targetText = dom.window.document.getElementById("tw-answ-target-text").textContent.trim();
        const detectedLanguage = dom.window.document.getElementById("tw-answ-detected-sl-name").textContent.trim();

        return { "source": sourceText, "target": targetText, "language:": detectedLanguage };
    } catch (error) {
        console.error("Error fetching translation:", error);
    }
};


app.get('/', (req, res) => {
    fetchTranslation(req.query.input).then((result) => {
        console.log(result);
        res.send(result);
    }).catch((error) => {
        console.error(error);
        res.send('Unable to translate...')
    });
})

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})