from init import db

"""
Domain.
"""

class Example(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)

    def __init__(self, name):
        self.name = name

    # Must be valid JSON serializable string
    def __repr__(self):
        return '{ id: %s, name: %r }' %(self.id, self.name)

"""
Queries.
"""

def scan_examples():
    return Example.query.all()

def get_example(id):
    return Example.query.get(id)

def delete_example(id):
    example = Example.query.get(id)
    db.session.delete(example)
    db.session.commit()
    return example

def update_example(id, name):
    example = Example.query.get(id)
    example.name = name
    db.session.commit()

    result = Example.query.get(id)
    return result

def create_example(name):
    example = Example(name)
    db.session.add(example)
    db.session.commit()

    return example

def prepopulate():
    db.drop_all()

    db.create_all()

    example_a = Example('example_a')
    db.session.add(example_a)

    example_b = Example('example_b')
    db.session.add(example_b)

    example_c = Example('example_c')
    db.session.add(example_c)

    example_d = Example('example_d')
    db.session.add(example_d)

    db.session.commit()
