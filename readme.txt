Database Schema Overview

The project uses a relational PostgreSQL database designed around daily growth tracking.

Core tables:

                    users – 
                    stores user identity and authentication data

                    mornings – 
                    daily morning check-in per user

                    morning_activities – 
                    tasks linked to a morning record

                    evenings – 
                    daily reflection per user

                    skills – 
                    long-term skills tracked by a user

                    skill_activities –
                    daily practice logs for skills

Relationships:

                    One user → many mornings

                    One morning → many morning activities

                    One user → many skills

                    One skill → many skill activities