<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
      form {
        border: 1px solid #999;
        border-radius: 4px;
        padding: 12px 8px;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 12px;
        max-width: 500px;
        margin: 128px auto 0;
      }

      label {
        display: flex;
        gap: 4px;
        width: 100%;
      }

      button {
        padding: 8px 16px;
        font-size: 16px;
        background-color: #710000;
        color: #fff;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        width: 100%;
      }
    </style>
  </head>
  <body>
    <form action="process.php" method="post">
      <h1>Select the items for your party:</h1>
      <div>
        <label for="cake">
          <input type="checkbox" name="cake" id="cake" value="0" />
          Cake
        </label>
        <br />
        <label for="balloons">
          <input type="checkbox" name="balloons" id="balloons" value="1" />
          Balloons
        </label>
        <br />
        <label for="music_system">
          <input
            type="checkbox"
            name="music_system"
            id="music_system"
            value="2"
          />
          Music System
        </label>
        <br />
        <label for="lights">
          <input type="checkbox" name="lights" id="lights" value="3" />
          Lights
        </label>
        <br />

        <label for="catering_service">
          <input
            type="checkbox"
            name="catering_service"
            id="catering_service"
            value="4"
          />
          Catering Service
        </label>
        <br />
        <label for="dj">
          <input type="checkbox" name="dj" id="dj" value="5" />
          DJ
        </label>
        <br />
        <label for="photo_booth">
          <input
            type="checkbox"
            name="photo_booth"
            id="photo_booth"
            value="6"
          />
          Photo Booth
        </label>
        <br />
        <label for="tables">
          <input type="checkbox" name="tables" id="tables" value="7" />
          Tables
        </label>
        <br />
        <label for="chairs">
          <input type="checkbox" name="chairs" id="chairs" value="8" />
          Chairs
        </label>
        <br />
        <label for="drinks">
          <input type="checkbox" name="drinks" id="drinks" value="9" />
          Drinks
        </label>
        <br />
        <label for="party_hats">
          <input type="checkbox" name="party_hats" id="party_hats" value="10" />
          Party Hats
        </label>
        <br />
        <label for="streamers">
          <input type="checkbox" name="streamers" id="streamers" value="11" />
          Streamers
        </label>
        <br />
        <label for="invitation_cards">
          <input
            type="checkbox"
            name="invitation_cards"
            id="invitation_cards"
            value="12"
          />
          Invitation Cards
        </label>
        <br />
        <label for="party_games">
          <input
            type="checkbox"
            name="party_games"
            id="party_games"
            value="13"
          />
          Party Games
        </label>
        <br />
        <label for="cleaning_service">
          <input
            type="checkbox"
            name="cleaning_service"
            id="cleaning_service"
            value="14"
          />
          Cleaning Service
        </label>
      </div>
      <br />
      <button type="submit">
        Calculate epicness
      </button>
    </form>
  </body>
</html>
