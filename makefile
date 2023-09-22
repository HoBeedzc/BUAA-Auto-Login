init:
	@read -p "Enter your BUAA username: " USERNAME 
	@read -p "Enter your BUAA password: " PASSWORD
	@echo "Write username and password into zsh profile..."
	@echo "# >>>>>>>>>> BUAA Auto Login init >>>>>>>>>>" >> ~/.zshrc
	@echo "export BUAA_USERNAME=$(USERNAME)" >> ~/.zshrc
	@echo "export BUAA_PASSWORD=$(PASSWORD)" >> ~/.zshrc
	@echo "# <<<<<<<<<< BUAA Auto Login init <<<<<<<<<<" >> ~/.zshrc
	@echo "init successfully!"

clean:
	@sed -i '/# >>>>>>>>>>BUAA auto login init<<<<<<<<<</,+2d' ~/.zshrc
	@echo "Cleanup zshrc"
