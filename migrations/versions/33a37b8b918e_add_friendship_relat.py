"""add friendship relationship

Revision ID: 33a37b8b918e
Revises: None
Create Date: 2013-04-23 14:47:32.396945

"""

# revision identifiers, used by Alembic.
revision = '33a37b8b918e'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('friendship',
    sa.Column('friend_me', sa.Integer(), nullable=False),
    sa.Column('friend_other', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['friend_me'], ['gwuser.id'], ),
    sa.ForeignKeyConstraint(['friend_other'], ['gwuser.id'], ),
    sa.PrimaryKeyConstraint('friend_me', 'friend_other')
    )
    op.drop_table(u'users')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table(u'users',
    sa.Column(u'id', sa.INTEGER(), server_default="nextval('users_id_seq'::regclass)", nullable=False),
    sa.Column(u'name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint(u'id', name=u'users_pkey')
    )
    op.drop_table('friendship')
    ### end Alembic commands ###