"""Autogenerated

Revision ID: bc03003108be
Revises: 
Create Date: 2024-06-13 09:04:57.190926

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bc03003108be'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Departments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('test', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('birth_date', sa.String(), nullable=True),
    sa.Column('position', sa.String(), nullable=True),
    sa.Column('salary', sa.Integer(), nullable=True),
    sa.Column('work_from', sa.DateTime(), nullable=True),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['Departments.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['Projects.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('emplo_proj',
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['Employees.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['Projects.id'], )
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('emplo_proj')
    op.drop_table('Employees')
    op.drop_table('Projects')
    op.drop_table('Departments')
    # ### end Alembic commands ###