package com.persistance.dao;

import org.springframework.stereotype.Repository;

import com.persistance.model.Utilisateur;

@Repository
public class UtilisateurDao extends AbstractHibernateDao<Utilisateur> implements
		IUtilisateurDao {

	public UtilisateurDao() {

		setClazz(Utilisateur.class);
	}

	// API

}
