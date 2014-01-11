tdaemon --custom-args='--ds chicken.settings.base --cov-config .coveragerc --cov . --cov-report xml --color yes' -t py

rsync -vramlHP ~/PycharmProjects/chicken_project/frontend/dist www@vegan-oasis.tk:~/Code/chicken_project/frontend