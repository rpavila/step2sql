from sqlalchemy import Column, Integer, String, DateTime, Text, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

__author__ = 'rpavila'

Base = declarative_base()

class Part(Base):
    __tablename__ = 'part'

    id = Column(Integer, primary_key=True)
    step_filename = Column(String)
    step_datetime = Column(DateTime)
    step_version = Column(String)
    step_author = Column(String)
    step_description = Column(Text)

    nodes = relationship("BRepNode", order_by="BRepNode.id", backref="part")

class BRepNode(Base):
    __tablename__ = 'b_rep_node'

    id = Column(Integer, primary_key=True)
    name = Column('node_name', String)
    part_id = Column(Integer, ForeignKey('part.id'))

    part = relationship("Part", backref=backref('nodes', order_by=id))

class BRepTree(Base):
    __tablename__ = 'b_rep_tree'

    id = Column(Integer, primary_key=True)
    left = Column('t_left', Integer)
    right = Column('t_right', Integer)
    node_id = Column(Integer, ForeignKey('b_rep_node.id'))

    node = relationship("BRepNode", backref=backref('trees', order_by=id))