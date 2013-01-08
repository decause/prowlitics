from sqlalchemy import create_engine
from knowledge.model import init_model, metadata, Entity, DBSession
from kitchen.text.converters import to_bytes, to_unicode

import sunlight

engine = create_engine('sqlite:///knowledge.db')
init_model(engine)
metadata.create_all(engine)

ny_legs = sunlight.openstates.legislators(state='ny')


def inject_test_knowledge():
    monster = Entity(u'Monster')
    fairy = Entity(u'Fairy')
    rjbean = Entity(u'rjbean')
    monster[u'color'] = u'Green'
    monster[u'name'] = u'Lotharrr'
    fairy[u'flies'] = True
    fairy[u'name'] = u'Bell'
    rjbean[u'name'] = u'ralph'
    rjbean[u'flies'] = False
    rjbean[u'hacks'] = True

    DBSession.add(monster)
    DBSession.add(fairy)
    DBSession.add(rjbean)
    DBSession.commit()


def inject_knowledge():
    #SunlightAPI returns nicely Unicoded data, but not all APIs will...
    #Don't forget to use to_unicode()
    knowledge = DBSession
    for leg in ny_legs:
        print leg['full_name']
        #Check if entity is already in DB, and if so continue
        #This is good for not duplicating entries, however
        #This will skip updates to the entity :(
        #This is why Sunlight included an "updated_at" field :)
        #TODO: Change check to "updated_at" instead of full_name
        if Entity.by_name(leg['full_name']):
            continue
            character = Entity.by_name(leg['full_name'])
        else:
            character = Entity(leg['full_name'])
        for key, value in leg.items():
            character[key] = to_unicode(value)
        knowledge.add(character)
        knowledge.commit()

inject_knowledge()


# Query all the Entities out of knowledge
def the_facts():
    knowledge_query = DBSession.query(Entity).all()
    for entity in knowledge_query:
        print to_bytes(entity), to_bytes(entity.facts.values())


the_facts()
