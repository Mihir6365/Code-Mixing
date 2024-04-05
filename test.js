let input = "This video good is";

input = encodeURIComponent(input);



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
    throw new Error('Network response was not ok.');
  }
}).then(data => {
  let answers = data.Sentences;
  for (let answer of answers) {
    console.log(answer.Sentence);
  }
}).catch(error => {
  console.error('There was a problem with the fetch operation:', error);
});
