# 2048 Game

This game is implemented in Python. It was created a Docker image to help the game execution. So the only thing you need to install on your machine is Docker.

## How to use

Build the image:
`make build`

Since `setup` rule is executed prior to `docker build` command, it is created the docker network when you execute this rule.
