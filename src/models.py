import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True) 
    name = Column(String(250))
    diameter = Column(String(250))
    rotation_period = Column(String(250))
    orbital_period = Column(String(250))
    gravity = Column(String(250))
    population = Column(String(250))
    climate = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(String(250))
    created = Column(String(250))
    edited = Column(String(250))
    people_id = Column(Integer, ForeignKey('people.id'))
    people = relationship(People)
    film_id = Column(Integer, ForeignKey('film.id'))
    film=relationship(Film)
    url = Column(String(250))

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    birth_year = Column(String(250))
    eye_color = Column(String(250))
    homeworld_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)
    gender = Column(String(250))
    hair_color = Column(String(250))
    height = Column(String(250))
    mass = Column(String(250))
    skin_color = Column(String(250))
    created = Column(String(250)) 
    url = Column(String(250))
    species_id = Column(Integer, ForeignKey('species.id'))
    species = relationship(Species)
    starships_id = Column(Integer, ForeignKey('starships.id'))
    starships=relationship(Starships)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicles=relationship(Vehicles)

class Film(Base):
    __tablename__ = 'film'
    id = Column(Integer, primary_key=True)
    people_id = Column(Integer, ForeignKey('people.id'))
    people = relationship(People)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)
    species_id = Column(Integer, ForeignKey('species.id'))
    species = relationship(Species)
    starships_id = Column(Integer, ForeignKey('starships.id'))
    starships=relationship(Starships)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicles=relationship(Vehicles)
    title = Column(String(250))
    episode_id = Column(String(250))
    opening_crawl = Column(String(250))
    director = Column(String(250))
    producer = Column(String(250))
    release_date = Column(String(250))
    created = Column(String(250))
    edited = Column(String(250))
    passengers = Column(String(250))
    max_atmosphering_speed = Column(String(250))
    cargo_capacity = Column(String(250))
    consumables = Column(String(250))
    created = Column(String(250))
    edited = Column(String(250))
    url = Column(String(250))


class Starships(Base):
    __tablename__ = 'starships'
    mglt = Column(String(250))
    cargo_capacity = Column(String(250))
    consumables = Column(String(250))
    created = Column(String(250))
    edited = Column(String(250))
    url = Column(String(250))
    cost_in_credits = Column(String(250))
    crew = Column(String(250))
    hyperdrive_rating = Column(String(250))
    length = Column(String(250))
    manufacturer = Column(String(250))
    max_atmosphering_speed = Column(String(250))
    model = Column(String(250))
    name = Column(String(250))
    passengers = Column(String(250))
    film_id = Column(Integer, ForeignKey('film.id'))
    film=relationship(Film)
    starship_class = Column(String(250))





class Vehicle(Base):
    __tablename__ = 'vehicle'
    cargo_capacity = Column(String(250))
    consumables = Column(String(250))
    created = Column(String(250))
    edited = Column(String(250))
    url = Column(String(250))
    cost_in_credits = Column(String(250))
    crew = Column(String(250))
    length = Column(String(250))
    manufacturer = Column(String(250))
    max_atmosphering_speed = Column(String(250))
    model = Column(String(250))
    name = Column(String(250))
    passengers = Column(String(250))
    film_id = Column(Integer, ForeignKey('film.id'))
    film=relationship(Film)
    people_id = Column(Integer, ForeignKey('people.id'))
    people = relationship(People)
    vehicle_class = Column(String(250))


class Species(Base):
    __tablename__ = 'species'
     average_height = Column(String(250))
    average_lifespan = Column(String(250))
    created = Column(String(250))
    edited = Column(String(250))
    url = Column(String(250))
    classification = Column(String(250))
    designation = Column(String(250))
    eye_colors = Column(String(250))
    hair_colors = Column(String(250))
    language = Column(String(250))
    skin_colors = Column(String(250))
    people_id = Column(Integer, ForeignKey('people.id'))
    people = relationship(People)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)
    film_id = Column(Integer, ForeignKey('film.id'))
    film=relationship(Film)

class PeopleFilm(Base):
    __tablename__ = 'people_film'
    people_id = Column(Integer, ForeignKey('people.id'), primary_key=True)
    people = relationship(People)
    film_id = Column(Integer, ForeignKey('film.id'), primary_key=True)
    film = relationship(Film)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png') 



