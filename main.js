const express = require('express');
const app = express();
const port = 3000;
const cors = require('cors');
app.use(cors());
const { spawn } = require('child_process');


app.get('/', (req, res) => {
    let input = req.query.string;
    const python = spawn('python', ['final_linked.py', input]);
    python.stdout.on('data', function (data) {
        dataToSend = data.toString();
        let input = encodeURIComponent(dataToSend);
        fetch(`https://rephrasesrv.gingersoftware.com/rephrase/rephrase?platform=ginger.web&s=${input}&size=6&lang=en`, {
            "headers": {
                "accept": "application/json",
                "accept-language": "en-IN,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6",
                "if-none-match": "W/\"26e-8SHMwRI2imiT7LGjbkB2YkIRTJg\"",
                "sec-ch-ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-site",
                "Referer": "https://www.gingersoftware.com/",
                "Referrer-Policy": "strict-origin-when-cross-origin"
            },
            "method": "GET"
        }).then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Result was not ok :/');
            }
        }).then(data => {
            let answers = data.Sentences;
            res.send(answers);
        }).catch(error => {
            console.error('There was a problem with the fetch operation:', error);
            res.send(error)
        });
    });
});

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`);
});