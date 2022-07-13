let url = "http://ip-api.com/json"

$httpClient.get(url, function (error, response, data) {
  let jsonData = JSON.parse(data)
  let country = jsonData.country
  let state = jsonData.regionName
  let city = jsonData.city
  let isp = jsonData.isp
  let ip = jsonData.query
  body = {
    title: 'IP Geolocation',
    content: `${city}, ${state}, ${country}\n${isp}`,
  backgroundColor: "#663399",
  icon: "network",
  }
  $done(body);
});
