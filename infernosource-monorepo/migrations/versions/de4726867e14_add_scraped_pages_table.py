"""Add scraped_pages table

Revision ID: de4726867e14
Revises: cb328a2d44f1
Create Date: 2025-07-11

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'de4726867e14'
down_revision = 'cb328a2d44f1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'scraped_pages',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('site_id', sa.Integer(), sa.ForeignKey('sites.id'), nullable=True),
        sa.Column('url', sa.String(), index=True, nullable=True),
        sa.Column('html_content', sa.Text(), nullable=True),
        sa.Column('extracted_text', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
    )


def downgrade():
    op.drop_table('scraped_pages')
