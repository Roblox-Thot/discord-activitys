<div align="center">

# github-activitys
[![Grab game list](https://github.com/Roblox-Thot/github-activitys/actions/workflows/run.yml/badge.svg)](https://github.com/Roblox-Thot/github-activitys/actions/workflows/run.yml)

</div>


JSON log of all the detectable apps for discord

Grabs the detected games from Discord's API `api/v9/applications/detectable` and pushes it to [json/detectable.json](json/detectable.json) every day.

## File types
- [json/executables.json](json/executables.json) and [text/executables.text](text/executables.txt) contains a list of the executable names
- [json/games.json](json/games.json) and [text/games.text](text/games.txt) contains a list of the game names

## TODO:
- [x] ~~Make a list of new games added~~ (Printed in the ran action)
- [x] ~~Don't commit if nothing has changed~~
- [x] ~~Find a way to have workflow not error if no files were changed~~
