from sqlalchemy import create_engine
from knowledge.model import init_model, metadata, Entity, DBSession
from kitchen.text.converters import to_unicode, to_bytes

import sunlight
engine = create_engine('sqlite:///knowledge.db')
init_model(engine)
metadata.create_all(engine)

# Query all the Entities out of knowledge
knowledge_query = DBSession.query(Entity).all()
for entity in knowledge_query:
    print to_bytes(entity), to_bytes(entity.facts.values())

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

    knowledge = DBSession
    for leg in ny_legs:
        character = Entity(u'%s' % to_unicode(leg['full_name']))
        character[u'name'] = (u'%s' % to_unicode(leg['full_name']))
        for key, value in leg.items():
            character[to_unicode(key)] = to_unicode(value)
        knowledge.add(character)
        knowledge.commit()

inject_knowledge()


# Query all the Entities out of knowledge
def the_facts():
    knowledge_query = DBSession.query(Entity).all()
    for entity in knowledge_query:
        print to_bytes(entity), to_bytes(entity.facts.values())

the_facts()
