const { parse } = require('url')

module.exports = (req, res) => {
  res.sendFile(__dirname + '/index2.html')
}
