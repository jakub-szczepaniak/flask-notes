drop table if exists documents;

create table documents (
    id integer primary key autoincrement,
    title text not null
);