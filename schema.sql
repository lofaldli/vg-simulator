drop table if exists entries;
create table entries (
    id integer primary key autoincrement,
    article_id text not null,
    title text not null,
    image_url not null
);
