"""Initial Migration

Revision ID: def753b21190
Revises: 
Create Date: 2021-06-23 18:13:53.607680

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'def753b21190'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('reviews', sa.String(length=255), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('roleUser', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fname', sa.String(length=128), nullable=True),
    sa.Column('sname', sa.String(length=128), nullable=True),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('phone', sa.Integer(), nullable=True),
    sa.Column('dataJoined', sa.DateTime(), nullable=True),
    sa.Column('pass_secure', sa.String(length=255), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('house',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(length=128), nullable=True),
    sa.Column('city', sa.String(length=128), nullable=True),
    sa.Column('images', sa.String(), nullable=True),
    sa.Column('house_type', sa.String(length=128), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('desc', sa.String(), nullable=True),
    sa.Column('dateposted', sa.DateTime(), nullable=True),
    sa.Column('user', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_roles')
    op.drop_table('house')
    op.drop_table('users')
    op.drop_table('roles')
    op.drop_table('reviews')
    # ### end Alembic commands ###
