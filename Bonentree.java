package com.persistance.model;

// Generated 7 mars 2016 19:36:24 by Hibernate Tools 3.4.0.CR1

import java.util.Date;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.Table;
import javax.persistence.Temporal;
import javax.persistence.TemporalType;

/**
 * Bonentree generated by hbm2java
 */
@Entity
@Table(name = "bonentree", catalog = "gestionstock")
public class Bonentree implements java.io.Serializable {

	private int identree;
	private Stock stock=new Stock();
	private Utilisateur utilisateur=new Utilisateur();
	private Date dateentree;
	private int prixunitaire;
	private Integer quantite;

	public Bonentree() {
	}

	public Bonentree(int identree, Stock stock, int prixunitaire) {
		this.identree = identree;
		this.stock = stock;
		this.prixunitaire = prixunitaire;
	}

	public Bonentree(int identree, Stock stock, Utilisateur utilisateur,
			Date dateentree, int prixunitaire, Integer quantite) {
		this.identree = identree;
		this.stock = stock;
		this.utilisateur = utilisateur;
		this.dateentree = dateentree;
		this.prixunitaire = prixunitaire;
		this.quantite = quantite;
	}

	@Id
	@Column(name = "IDentree", unique = true, nullable = false)
	public int getIdentree() {
		return this.identree;
	}

	public void setIdentree(int identree) {
		this.identree = identree;
	}

	@ManyToOne(fetch = FetchType.EAGER)
	@JoinColumn(name = "refP", nullable = false)
	public Stock getStock() {
		return this.stock;
	}

	public void setStock(Stock stock) {
		this.stock = stock;
	}

	@ManyToOne(fetch = FetchType.LAZY)
	@JoinColumn(name = "agent")
	public Utilisateur getUtilisateur() {
		return this.utilisateur;
	}

	public void setUtilisateur(Utilisateur utilisateur) {
		this.utilisateur = utilisateur;
	}

	@Temporal(TemporalType.TIMESTAMP)
	@Column(name = "dateentree", length = 0)
	public Date getDateentree() {
		return this.dateentree;
	}

	public void setDateentree(Date dateentree) {
		this.dateentree = dateentree;
	}

	@Column(name = "prixunitaire", nullable = false)
	public int getPrixunitaire() {
		return this.prixunitaire;
	}

	public void setPrixunitaire(int prixunitaire) {
		this.prixunitaire = prixunitaire;
	}

	@Column(name = "quantite")
	public Integer getQuantite() {
		return this.quantite;
	}

	public void setQuantite(Integer quantite) {
		this.quantite = quantite;
	}

}
