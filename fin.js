const express = require('express');
const app = express();
const port = 3000;
const cors = require('cors');
app.use(cors());


app.get('/', (req, res) => {
  let input = encodeURIComponent(req.query.string);
  fetch("https://www.google.com/async/translate?vet=12ahUKEwjyxO_2sIeFAxUzT2wGHeJ_BU8QqDh6BAgSEDA..i&ei=8Tf9ZbKIC7OeseMP4v-V-AQ&opi=89978449&rlz=1C1OPNX_en-GBIN1080IN1080&yv=3&cs=1", {
    "headers": {
      "accept": "*/*",
      "accept-language": "en-IN,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6",
      "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
      "sec-ch-ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Google Chrome\";v=\"122\"",
      "sec-ch-ua-arch": "\"x86\"",
      "sec-ch-ua-bitness": "\"64\"",
      "sec-ch-ua-full-version": "\"122.0.6261.131\"",
      "sec-ch-ua-full-version-list": "\"Chromium\";v=\"122.0.6261.131\", \"Not(A:Brand\";v=\"24.0.0.0\", \"Google Chrome\";v=\"122.0.6261.131\"",
      "sec-ch-ua-mobile": "?0",
      "sec-ch-ua-model": "\"\"",
      "sec-ch-ua-platform": "\"Windows\"",
      "sec-ch-ua-platform-version": "\"15.0.0\"",
      "sec-ch-ua-wow64": "?0",
      "sec-fetch-dest": "empty",
      "sec-fetch-mode": "cors",
      "sec-fetch-site": "same-origin",
      "x-client-data": "CKW1yQEIjbbJAQimtskBCKmdygEIiOHKAQiSocsBCP6YzQEIhaDNAQjd7s0BCOL6zQEI2oTOARiY9c0BGJ74zQEY0YLOAQ==",
      "x-dos-behavior": "Embed"
    },
    "referrer": "https://www.google.com/",
    "referrerPolicy": "origin",
    "body": `async=translate,sl:auto,tl:en,st:${input},id:1711091873697,qc:true,ac:true,_id:tw-async-translate,_pms:s,_fmt:pc`,
    "method": "POST",
    "mode": "cors",
    "credentials": "include"
  }).then(response => response.text())
    .then(data => {
      let str = data;
      let match = str.match(/<span id="tw-answ-target-text">(.*?)<\/span>/);
      let translatedText = match ? match[1] : 'No match found';
      console.log(translatedText);
      res.send({ result: translatedText });
    })
    .catch(() => {
      res.send({ result: translatedText });
    });
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});