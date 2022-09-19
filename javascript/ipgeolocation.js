let url = "http://ip-api.com/json"

$httpClient.get(url, function (error, response, data) {
  let jsonData = JSON.parse(data)
  let country = jsonData.country
  let state = jsonData.regionName
  let city = jsonData.city
  let isp = jsonData.isp
  let ip = jsonData.query
  body = {
    title: `${country}`,
    content: `${state}\n${city}\n${isp}`,
    backgroundColor: "#737373",
    icon: "location",
  }$done(body);
});
