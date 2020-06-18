# STEM Bot
This Discord bot exists to help with problems related to Science, Technology, Engineering, and Math.

## Commands
### Science
* `element`: Get a specific element by atomic number, symbol, or name
  * Aliases: `e`, `el`, `elem`
  * Arguments:
    * `element_input`: An atomic number, element symbol, or element name

### Mathematics
* `sigfigs`: Round a number to a specified number of significant figures
  * Aliases: `sf`, `sfs`
  * Arguments:
    * `number`: Number to round
    * `figures`: Number of significant figures to round to

### Utilities
* `ping`: Check the bot's latency
  * Aliases: `pong`
  * Arguments: *None*
* `wikipedia`: Get a summary from Wikipedia
  * Aliases: `w`, `wp`, `wikipedia`
  * Arguments:
    * `search_term`: What to search for
* `steal`: Steal a custom emoji
  * Aliases: *None*
  * Arguments: *None*
  * Permissions required:
    * User:
      * `add_reactions`
      * `external_emojis`
      * `manage_emojis`
    * Bot:
      * `manage_emojis`