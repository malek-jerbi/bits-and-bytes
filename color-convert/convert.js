const fs = require('fs')

fs.readFile('simple.css', 'utf8', function (err, data) {
  if (err) {
    console.error(err)
    return
  }
  let regex = /#[0-9a-fA-F]{6}/gi // matches any CSS color codes of 6 characters long (after #)
  let newStr = data.replace(regex, 'newnew')
  console.log(newStr)
})
