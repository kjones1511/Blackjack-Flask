// todo: reminder to use this for loading from URL https://stackoverflow.com/questions/2177548/load-json-into-variable
/*
	Blackjack 21
	A simple game developed using Javascript, HTML and CSS
	@author Stayko Chalakov
*/
//namespacing
var BlackjackJS = (function() {

	//imports game details as JSON, TODO replace with a while loop checking for updates every second
	const cookie = "56565656565656"
	const ID = "edbd9d8a-9244-11ea-bb37-0242ac130002"
	const urlPlayer = ("http://localhost:5000/tableUpdate/".concat(cookie));
	const urlGameState = "http://localhost:5000/gameInfoUpdate/".concat(ID);

	//button push URLs
	const urlHit = "http://localhost:5000/hit";
	const urlDouble = "http://localhost:5000/double";
	const urlStand = "http://localhost:5000/stand";
	const urlSplit = "http://localhost:5000/split";
	const request = {
		"ID": "edbd9d8a-9244-11ea-bb37-0242ac130002"
	};

	this.jsonRetrieve = function (url) {
		var json = null;
		$.ajax({
			'async': false,
			'global': false,
			'url': url,
			'dataType': "json",
			'success': function (data) {
				json = data;
			}
		});
		return json;
	}

	this.postJSON = function(url, request){
		$.ajax({
			url: url,
			type: 'POST',
			dataType: 'json',
			contentType: "application/json; charset=utf-8",
			data: JSON.stringify(request)
		});
	}
	
	//JSON objects used throughout game
	var playerJSON = this.jsonRetrieve(urlPlayer);  
	var gameStateJSON = this.jsonRetrieve(urlGameState);  
	/**************
		Card class
	***************/

	/*
		Constructor
		@param {String} value
		@param {String} suit
	*/
	function Card(value, suit){
		this.value = value;
	  this.suit = suit;
	}

	/*Renders the card*/
	Card.prototype.view = function(){
		var htmlEntities = {
			'H' : '&#9829;',
			'D' : '&#9830;',
			'C' : '&#9827;',
			'S' : '&#9824;'
		}
		//resolves mismatch b/w Python face card values (number) and expected JS string values
		if (this.value == '11'){ this.value = 'J'};
		if (this.value == '12'){ this.value = 'Q'};
		if (this.value == '13'){ this.value = 'K'};
		if (this.value == '14'){ this.value = 'A'};
		return `
			<div class="card ` + this.suit + `">
				<div class="top rank">` + this.value + `</div>
				<div class="suit">` + htmlEntities[this.suit] + `</div>
				<div class="bottom rank">` + this.value + `</div>
			</div>
		`;
	}

	/*************************** End of Card class ********************************/

	/***************
		Player class
	***************/

	/*
		Constructor
		@param {String} element - The DOM element
		@param {Array} hand - the array which holds all the cards
	*/
	function Player(element, hand){
		this.hand = hand;
		this.element = element;
	}

	Player.prototype.hit = function(card){
		this.hand.push(card);
	}
	/*
		Returns the array (hand) of cards
	*/
	Player.prototype.showHand = function(){
		var hand = "";
		for(var i = 0; i < this.hand.length; i++){
			 hand += this.hand[i].view();
		}
		return hand;
	}

	/*************************** End of Player class ******************************/

	/*************************
		Game - Singleton class
	**************************/

	var Game = new function(){

		/*
			Deal button event handler
		*/
		this.dealButtonHandler = function(){
			Game.start();
			this.dealButton.disabled = true;
			this.hitButton.disabled = false;
			this.standButton.disabled = false;
		}

		/*
			Hit button event handler
		*/
		this.hitButtonHandler = function(){
			postJSON(urlHit, request);
		}
			
		

		/*
			Stand button event handler
		*/
		this.standButtonHandler = function(){
			this.hitButton.disabled = true;
			this.standButton.disabled = true;

			
				//TODO needs to be expanded..

			}
		
		this.renderTable = function(){
			console.log("called renderTable");
			var playerJSON = jsonRetrieve(urlPlayer);  
			var gameStateJSON = jsonRetrieve(urlGameState);  
			console.log(playerJSON)			
			
			var dealerScore = playerJSON.currentHand[0].dealerScore;
			var playerScore = playerJSON.currentHand[0].score;
			var dealerHand = playerJSON.currentHand[0].dealerHand[0].hand;
			var playerHand = playerJSON.currentHand[0].hand;
				//TODO needs to be expanded..
			this.dealerScore.innerHTML = dealerScore;
			this.playerScore.innerHTML = playerScore;
			
			document.getElementById(this.player.element).innerHTML = [];
			document.getElementById(this.dealer.element).innerHTML = [];
			//array to loop through cards to render
			//document.getElementById(this.player.element).innerHTML += card.view();
			playerHand.forEach(
				card => document.getElementById(this.player.element).innerHTML += new Card( card.value, card.suit).view());
			if  (gameStateJSON.state == "gameOver"){
			dealerHand.forEach(
				card => document.getElementById(this.dealer.element).innerHTML += new Card( card.value, card.suit).view());}
			else {
			dealerHand.slice(1).forEach(
				card => document.getElementById(this.dealer.element).innerHTML += new Card( card.value, card.suit).view());}
			}
				
		

		this.loadButtonHandler = function(){
			console.log("made it to load button");
			this.renderTable();
		}
		
		/*
			Initialise
		*/
		this.init = function(){
			//var json = require('./content.json');
			console.log(playerJSON);
			var score = playerJSON.currentHand[0].score

			this.dealerScore = document.getElementById('dealer-score').getElementsByTagName("span")[0];
			this.playerScore = document.getElementById('player-score').getElementsByTagName("span")[0];
			this.dealButton = document.getElementById('deal');
			this.hitButton = document.getElementById('hit');
			this.standButton = document.getElementById('stand');
			this.loadButton = document.getElementById('load');

			//attaching event handlers
			this.dealButton.addEventListener('click', this.dealButtonHandler.bind(this));
			this.hitButton.addEventListener('click', this.hitButtonHandler.bind(this));
			this.standButton.addEventListener('click', this.standButtonHandler.bind(this));
			this.loadButton.addEventListener('click', this.loadButtonHandler.bind(this));
		
		}

		/*
			Start the game
		*/
		this.start = function(){

			//builds new dealer with no cards
			this.dealer = new Player('dealer', []);

			//builds new player
			this.player = new Player('player', []);


			//render the cards
			document.getElementById(this.dealer.element).innerHTML = this.dealer.showHand();
			document.getElementById(this.player.element).innerHTML = this.player.showHand();

			//renders the current scores
			this.dealerScore.innerHTML = 0;
			this.playerScore.innerHTML = 0;

			this.setMessage("Hit or Stand");
		}

		/*
			Instructions or status of game
		*/
		this.setMessage = function(str){
			document.getElementById('status').innerHTML = str;
		}


	}

	//Exposing the Game.init function
	//to the outside world
	return {
		init: Game.init.bind(Game)
	}

})()
