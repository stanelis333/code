"""Autogenerated2

Revision ID: 84c0333e384f
Revises: bc03003108be
Create Date: 2024-06-13 09:06:34.424709

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84c0333e384f'
down_revision: Union[str, None] = 'bc03003108be'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Projects', sa.Column('tes2', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Projects', 'tes2')
    # ### end Alembic commands ###
