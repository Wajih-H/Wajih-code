package com.persistance.model;

// Generated 7 mars 2016 19:36:24 by Hibernate Tools 3.4.0.CR1

import java.util.HashSet;
import java.util.Set;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.Id;
import javax.persistence.OneToMany;
import javax.persistence.Table;

/**
 * Categorie generated by hbm2java
 */
@Entity
@Table(name = "categorie", catalog = "gestionstock")
public class Categorie implements java.io.Serializable {

	private int idcategorie;
	private String libelle;
	private Set<Stock> stocks = new HashSet<Stock>(0);

	public Categorie() {
	}

	public Categorie(int idcategorie) {
		this.idcategorie = idcategorie;
	}

	public Categorie(int idcategorie, String libelle, Set<Stock> stocks) {
		this.idcategorie = idcategorie;
		this.libelle = libelle;
		this.stocks = stocks;
	}

	@Id
	@Column(name = "idcategorie", unique = true, nullable = false)
	public int getIdcategorie() {
		return this.idcategorie;
	}

	public void setIdcategorie(int idcategorie) {
		this.idcategorie = idcategorie;
	}

	@Column(name = "libelle")
	public String getLibelle() {
		return this.libelle;
	}

	public void setLibelle(String libelle) {
		this.libelle = libelle;
	}

	@OneToMany(fetch = FetchType.EAGER, mappedBy = "categorie")
	public Set<Stock> getStocks() {
		return this.stocks;
	}

	public void setStocks(Set<Stock> stocks) {
		this.stocks = stocks;
	}

}
