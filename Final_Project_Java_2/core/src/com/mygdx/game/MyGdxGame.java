package com.mygdx.game;

import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Input;
import com.badlogic.gdx.audio.Music;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.Sprite;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.utils.ScreenUtils;

import java.util.Random;

import com.mygdx.game.MyGame.Game;

public class MyGdxGame extends ApplicationAdapter {
    SpriteBatch batch;
    Texture fon, crossBowMan, mage, monk, peasant, rouge, sniper, spearMan;
    Music music;
    Game game;

    int turnCount = 0;


    @Override
    public void create() {
        game = new Game();
        game.createTeams();

        batch = new SpriteBatch();
        fon = new Texture("фоны/" + Fons.values()[new Random().nextInt(Fons.values().length)] + ".png");
        music = Gdx.audio.newMusic(Gdx.files.internal("Музыка/" + Muslo.values()[new Random().nextInt(Muslo.values().length)] + ".mp3"));
        music.setLooping(true);
        music.setVolume(0.05f);
        music.play();

        crossBowMan = new Texture("персонажи/CrossBowMan.png");
        mage = new Texture("персонажи/Mage.png");
        monk = new Texture("персонажи/Monk.png");
        peasant = new Texture("персонажи/Peasant.png");
        rouge = new Texture("персонажи/Rouge.png");
        sniper = new Texture("персонажи/Sniper.png");
        spearMan = new Texture("персонажи/SpearMan.png");
    }

    @Override
    public void render() {
        if (game.gameEnded()) {
            if (game.whoWin())
                fon = new Texture("фоны/GameEnd1.png");
            else fon = new Texture("фоны/GameEnd2.png");
            Gdx.graphics.setTitle(String.valueOf("Игра закончена"));
            ScreenUtils.clear(1, 0, 0, 1);
            batch.begin();
            batch.draw(fon, 0, 0, Gdx.graphics.getWidth(), Gdx.graphics.getHeight());
            batch.end();
            return;
        }

        if (Gdx.input.isButtonJustPressed(Input.Buttons.LEFT)) {
            game.teamsMakeTurns();
            Gdx.graphics.setTitle(String.valueOf("Ход № " + turnCount++));
        }

        ScreenUtils.clear(1, 0, 0, 1);
        batch.begin();
        batch.draw(fon, 0, 0, Gdx.graphics.getWidth(), Gdx.graphics.getHeight());
        for (int i = 9; i >= 0; i--) {
            batch.setColor(1, 1, 1, 1);
            if (game.holyTeam.get(i).getState().equals("Dead")) batch.setColor(Color.RED);
            int x = game.holyTeam.get(i).getPosition().getX() * Gdx.graphics.getWidth() / 12;
            int y = (game.holyTeam.get(i).getPosition().getY() - 1) * Gdx.graphics.getHeight() / 12;
            switch (game.holyTeam.get(i).getClassName()) {
                case "Арбалетчик":
                    batch.draw(crossBowMan, x, y);
                    break;
                case "Волшебник":
                    batch.draw(mage, x, y);
                    break;
                case "Монах":
                    batch.draw(monk, x, y);
                    break;
                case "Фермер":
                    batch.draw(peasant, x, y);
                    break;
                case "Разбойник":
                    batch.draw(rouge, x, y);
                    break;
                case "Лучник":
                    batch.draw(sniper, x, y);
                    break;
                case "Копейщик":
                    batch.draw(spearMan, x, y);
            }

            batch.setColor(1, 1, 1, 1);
            Sprite sprite = new Sprite();
            x = game.darkTeam.get(i).getPosition().getX() * Gdx.graphics.getWidth() / 12;
            y = (game.darkTeam.get(i).getPosition().getY() - 1) * Gdx.graphics.getHeight() / 12;
            switch (game.darkTeam.get(i).getClassName()) {
                case "Арбалетчик":
                    sprite = new Sprite(crossBowMan);
                    sprite.setPosition(x, y);
                    sprite.flip(true, false);
                    break;
                case "Волшебник":
                    sprite = new Sprite(mage);
                    sprite.setPosition(x, y);
                    sprite.flip(true, false);
                    break;
                case "Монах":
                    sprite = new Sprite(monk);
                    sprite.setPosition(x, y);
                    sprite.flip(true, false);
                    break;
                case "Фермер":
                    sprite = new Sprite(peasant);
                    sprite.setPosition(x, y);
                    sprite.flip(true, false);
                    break;
                case "Разбойник":
                    sprite = new Sprite(rouge);
                    sprite.setPosition(x, y);
                    sprite.flip(true, false);
                    break;
                case "Лучник":
                    sprite = new Sprite(sniper);
                    sprite.setPosition(x, y);
                    sprite.flip(true, false);
                    break;
                case "Копейщик":
                    sprite = new Sprite(spearMan);
                    sprite.setPosition(x, y);
                    sprite.flip(true, false);
            }
            if (game.darkTeam.get(i).getState().equals("Dead")) sprite.setColor(Color.RED);
            sprite.draw(batch);
        }
        batch.setColor(1, 1, 1, 1);
        batch.end();
    }

    @Override
    public void dispose() {
        batch.dispose();
        fon.dispose();
    }
}
