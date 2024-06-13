import click
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.hotel import Hotel
from models.room import Room
from models.guest import Guest
from database_setup import DATABASE_URL

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    pass

@click.command()
@click.argument('name')
def add_hotel(name):
    hotel = Hotel(name=name)
    session.add(hotel)
    session.commit()
    click.echo(f'Hotel {name} added.')

@click.command()
@click.argument('room_number')
@click.argument('hotel_id')
def add_room(room_number, hotel_id):
    room = Room(room_number=room_number, hotel_id=hotel_id)
    session.add(room)
    session.commit()
    click.echo(f'Room {room_number} added to hotel ID {hotel_id}.')

@click.command()
@click.argument('nationality')
@click.argument('room_id')
def add_guest(nationality, room_id):
    guest = Guest(nationality=nationality, room_id=room_id)
    session.add(guest)
    session.commit()
    click.echo(f'Guest with nationality {nationality} added to room ID {room_id}.')

@click.command()
def list_hotels():
    hotels = session.query(Hotel).all()
    for hotel in hotels:
        click.echo(f'Hotel ID: {hotel.id}, Name: {hotel.name}')

@click.command()
@click.argument('hotel_id')
def list_rooms(hotel_id):
    rooms = session.query(Room).filter_by(hotel_id=hotel_id).all()
    for room in rooms:
        click.echo(f'Room ID: {room.id}, Room Number: {room.room_number}, Hotel ID: {room.hotel_id}')

@click.command()
@click.argument('room_id')
def list_guests(room_id):
    guests = session.query(Guest).filter_by(room_id=room_id).all()
    for guest in guests:
        click.echo(f'Guest ID: {guest.id}, Nationality: {guest.nationality}, Room ID: {guest.room_id}')

cli.add_command(add_hotel)
cli.add_command(add_room)
cli.add_command(add_guest)
cli.add_command(list_hotels)
cli.add_command(list_rooms)
cli.add_command(list_guests)

if __name__ == '__main__':
    cli()
