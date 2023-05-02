DROP TABLE IF EXISTS usuarios;

DROP TABLE IF EXISTS materiais;

DROP TABLE IF EXISTS solicitacoes;

DROP TABLE IF EXISTS reservas;

DROP TYPE IF EXISTS permissoes;

DROP TYPE IF EXISTS status_solicitacao;

CREATE TYPE permissoes AS ENUM ('admin', 'user');

CREATE TYPE status_solicitacao AS ENUM ('pendente', 'aprovado', 'rejeitado');

CREATE TABLE IF NOT EXISTS usuarios (
	id SERIAL PRIMARY KEY,
	nome VARCHAR(60) NOT NULL,
	email VARCHAR(60) NOT NULL UNIQUE,
	senha VARCHAR(60) NOT NULL,
	permissao permissoes NOT NULL DEFAULT 'user'
);

CREATE TABLE IF NOT EXISTS materiais (
	id SERIAL PRIMARY KEY,
	nome VARCHAR(60) NOT NULL,
	descricao VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS estoques (
	id SERIAL PRIMARY KEY,
	material_id INTEGER REFERENCES materiais (id),
	quantidate INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS solicitacoes (
	id SERIAL PRIMARY KEY,
	nome_gerencia_curso VARCHAR(200) NOT NULL,
	data_criacao TIMESTAMP WITH TIME ZONE DEFAULT now(),
	data_atualizacao TIMESTAMP WITH TIME ZONE DEFAULT now(),
	usuario_aprovador_id INTEGER REFERENCES usuarios (id) ON DELETE CASCADE,
	usuario_solicitante_id INTEGER REFERENCES usuarios (id) ON DELETE CASCADE,
	reservas INTEGER,
	status status_solicitacao DEFAULT 'pendente'
);

CREATE TABLE IF NOT EXISTS reservas (
	solicitacao_id INTEGER REFERENCES solicitacoes (id) ON DELETE CASCADE,
	material_id INTEGER REFERENCES materiais (id) ON DELETE CASCADE,
	quantidate_reservada INTEGER NOT NULL,
	PRIMARY KEY (solicitacao_id, material_id)
);

ALTER TABLE solicitacoes
ADD CONSTRAINT fk_reservas FOREIGN KEY (id, reservas) REFERENCES reservas (solicitacao_id, material_id) ON DELETE CASCADE;