const Discord = require('discord.js')
const client = new Discord.Client()
const config = require('./config.json')
const readline = require('readline-sync')

let Token = readline.question("Token: ")
let Role_Name = readline.question("Role Name: ")
let guildID = readline.question("Server ID: ")

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

client.on('message', msg => {
  if (msg.content === "&start"){
    var colors = []
    for(let i = 0; i<= colors.length; i++){
      var role = message.guild.roles.find(role => role.name === Role_Name)
      setInterval(() => {
        role.edit({
          color : colors[i]
        })
      }, 5000);
    }
  }
})
client.login(Token)
