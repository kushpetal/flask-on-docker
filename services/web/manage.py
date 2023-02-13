from flask.cli import FlaskGroup

from project import app, db, User


cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command("seed_db")
def seed_db():
    db.session.add(User(email="michael@mherman.org"))
    db.session.commit()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
    cli()
