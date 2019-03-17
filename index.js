const { parse } = require('url')

module.exports = (req, res) => {
  res.sendFile('index2.html')
}
