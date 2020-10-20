const Discord = require('discord.js')
const client = new Discord.Client()
const readline = require('readline-sync')
const sleep = require('system-sleep')

let Token = readline.question("Token: ")
let Role_Name = readline.question("Role Name: ")

client.on('ready', () => {
  console.log(`
  ------------------------------------------------------------------------
  Developer: Leo Power
  GitHub: https://github.com/powerthecoder
  Website: https://powerthecoder.xyz/

  Disclaimer:
  This program can get your Discord account terminated and should
  be used at your own risk. Anything that you do or happens to you
  is not the developer Leo Power's fault. This was made for educational
  purposes only!
  ------------------------------------------------------------------------
  type &start in Discord to start the rainbow role
  `)
  console.log(" ")
  console.log("Bot Online")
})

client.on('message', message => {
  if(message.content === "&start"){
    var x = 0
    while (x != 1){
      sleep(5*1000)
      let colors = [0xff0000, 0xff9f00, 0x72ff00, 0x00ff6d, 0x00acff, 0x0200ff, 0xc500ff, 0xff0053]
      let role = message.guild.roles.cache.find(role => role.name === Role_Name) //Role_Name
      //let role = message.guild.roles.find(Role_Name, "name")
      var random_color = Math.floor(Math.random() * colors.length)
        role.edit({
          color : colors[random_color]
        })
    }
  }
})
client.login(Token) //Token
