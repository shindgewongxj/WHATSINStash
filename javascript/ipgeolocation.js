$httpClient.get("http://ip-api.com/json/?fields=regionName,country", function (error, response, data) {
    $done({
        title: "Unknown Geolocation",
        content: data,
        backgroundColor: "#663399",
        icon: "network",
    })
})
